#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Copyright (c) 2025 Huawei Technologies Co., Ltd.
# This file is part of the MindStudio project.
#
# MindStudio is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#
#    http://license.coscl.org.cn/MulanPSL2
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.
# -------------------------------------------------------------------------

import os
import unittest
import logging
import shutil
import sys

import test_base

logging.basicConfig(level=logging.INFO,
                    format='\n%(asctime)s %(filename)s [line:%(lineno)d] [%(levelname)s] %(message)s')


class MsptiActivityCallbackCase(test_base.TestProfiling):
    def __init__(self):
        super(MsptiActivityCallbackCase, self).__init__("execute")
        self.__result = ""
        self.id = "test_MsptiActivityCallbackCase"
        self.case_path = os.path.join(self.cfg_path.mspti_base_testcase_path, "activity_callback_all")
        self.res_dir = os.path.join(self.res_dir, self.id)
        self.build_path = os.path.join(self.case_path, "build")
        self.plog_path = os.path.join(self.build_path, "plog.txt")
        self.exec_cmd = f"cmake -S {self.case_path} -B {self.build_path} -DASCEND_HOME_PATH={self.cfg_path.ascend_home_path}; \
        make -C {self.build_path} -j$(nproc); {self.build_path}/main > {self.plog_path}"

    def initTest(self):
        self.logger.info("------------------------------- "
                           "Start execute case {} -------------------------------".format(self.id))
        if os.path.exists(self.res_dir):
            shutil.rmtree(self.res_dir)
        os.makedirs(self.res_dir)
        if os.path.exists(self.build_path):
            shutil.rmtree(self.build_path)
        os.makedirs(self.build_path)

    def checkRes(self):
        self.view_plog_error(self.plog_path)
        if self.res == 0:
            self.__result = self.cfg_value.pass_res
        else:
            self.__result = self.cfg_value.fail_res
        # 记录执行结果到result.txt
        self.write_res(self.id, self.__result)
        self.assertTrue(self.cfg_value.pass_res == self.__result)

    def execute(self):
        # 初始化工作空间
        self.initTest()
        # 执行用例
        self.executeCmd()
        # 执行结果校验
        self.checkRes()


class MsptiMarkMultiThreadCase(test_base.TestProfiling):
    def __init__(self):
        super(MsptiMarkMultiThreadCase, self).__init__("execute")
        self.__result = ""
        self.id = "test_MsptiMarkMultiThreadCase"
        self.case_path = os.path.join(self.cfg_path.mspti_base_testcase_path, "mark_multithread")
        self.res_dir = os.path.join(self.res_dir, self.id)
        self.build_path = os.path.join(self.case_path, "build")
        self.plog_path = os.path.join(self.build_path, "plog.txt")
        self.thread_num = 16
        self.mark_num_per_thread = 40000
        self.exec_cmd = f"cmake -S {self.case_path} -B {self.build_path} -DASCEND_HOME_PATH={self.cfg_path.ascend_home_path}; \
        make -C {self.build_path} -j$(nproc); {self.build_path}/main {self.thread_num} > {self.plog_path}"

    def initTest(self):
        self.logger.info("------------------------------- "
                           "Start execute case {} -------------------------------".format(self.id))
        if os.path.exists(self.res_dir):
            shutil.rmtree(self.res_dir)
        os.makedirs(self.res_dir)
        if os.path.exists(self.build_path):
            shutil.rmtree(self.build_path)
        os.makedirs(self.build_path)

    def get_mark_num(self):
        cmd = r"grep -r 'MSPTI_SMOKE_MARK_NUM' {0}".format(self.plog_path)
        status, res = self.subprocess_cmd(cmd)
        return res.split(" ")[1] if status == 0 else 0

    def checkRes(self):
        self.view_plog_error(self.plog_path)
        mark_num = int(self.get_mark_num())
        if mark_num != self.thread_num * self.mark_num_per_thread:
            self.logger.error(f"Execute {self.id} failed. mark total num error.")
            self.res += 1
        if self.res == 0:
            self.__result = self.cfg_value.pass_res
        else:
            self.__result = self.cfg_value.fail_res
        self.write_res(self.id, self.__result)
        self.assertTrue(self.cfg_value.pass_res == self.__result)

    def execute(self):
        # 初始化工作空间
        self.initTest()
        # 执行用例
        if self.executeCmd() != 0:
            self.logger.error(f"Execute {self.id} failed.")
            self.res += 1
        # 执行结果校验
        self.checkRes()


class MsptiPythonMonitorCase(test_base.TestProfiling):
    def __init__(self):
        super(MsptiPythonMonitorCase, self).__init__("execute")
        self.__result = ""
        self.id = "test_MsptiPythonMonitorCase"
        self.case_path = os.path.join(self.cfg_path.mspti_base_testcase_path, "monitor_minst")
        self.res_dir = os.path.join(self.res_dir, self.id)
        self.plog_path = os.path.join(self.res_dir, "plog.txt")
        self.exec_cmd = f"cd {self.case_path};" \
                        r"python3 mnist.py --addr='127.0.0.1' --workers 160 --lr 0.8 --print-freq 1 --dist-url 'tcp://127.0.0.1:50005' " \
                        r"--dist-backend 'hccl' --multiprocessing-distributed --world-size 1 --epochs 1 --rank 0 --device-list '4,5,6,7' --amp " \
                        f"--output {self.res_dir} > {self.plog_path}"

    def initTest(self):
        self.logger.info("------------------------------- "
                           "Start execute case {} -------------------------------".format(self.id))
        if os.path.exists(self.res_dir):
            shutil.rmtree(self.res_dir)
        os.makedirs(self.res_dir)

    def check_marker_count(self):
        marker_count_set = set()
        for csv_file in [path for path in os.listdir(self.res_dir) if path.endswith('csv')]:
            csv_file = os.path.join(self.res_dir, csv_file)
            cmd = "grep -r 'MSPTI_ACTIVITY_KIND_MARKER' {0} | wc -l".format(csv_file)
            status, res = self.subprocess_cmd(cmd)
            marker_count_set.add(int(res) if status == 0 else 0)
        self.logger.info(f"MarkerData count {marker_count_set}.")
        if len(marker_count_set) != 1:
            self.logger.error(f"Execute {self.id} failed. MarkerData num error.")
            self.res += 1

    def check_hccl_count(self):
        hccl_count_set = set()
        for csv_file in [path for path in os.listdir(self.res_dir) if path.endswith('csv')]:
            csv_file = os.path.join(self.res_dir, csv_file)
            cmd = "grep -r 'MSPTI_ACTIVITY_KIND_HCCL' {0} | wc -l".format(csv_file)
            status, res = self.subprocess_cmd(cmd)
            hccl_count_set.add(int(res) if status == 0 else 0)
        self.logger.info(f"HcclData count {hccl_count_set}.")
        if len(hccl_count_set) != 1:
            self.logger.error(f"Execute {self.id} failed. HcclData num error.")
            self.res += 1

    def checkRes(self):
        self.view_plog_error(self.plog_path)
        self.check_marker_count()
        self.check_hccl_count()
        if self.res == 0:
            self.__result = self.cfg_value.pass_res
        else:
            self.__result = self.cfg_value.fail_res
        self.write_res(self.id, self.__result)
        self.assertTrue(self.cfg_value.pass_res == self.__result)

    def execute(self):
        # 初始化工作空间
        self.initTest()
        # 执行用例
        if self.executeCmd() != 0:
            self.logger.error(f"Execute {self.id} failed.")
            self.res += 1
        # 执行结果校验
        self.checkRes()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MsptiActivityCallbackCase())
    suite.addTest(MsptiMarkMultiThreadCase())
    suite.addTest(MsptiPythonMonitorCase())
    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)
    if not test_result.wasSuccessful():
        sys.exit(1)
    else:
        sys.exit(0)

#!/bin/bash
# install constant
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
set -e
install_path=${1}
package_arch=${2}
install_for_all_flag=${3}
pylocal=y

function get_right() {
    if [ "$install_for_all_flag" = 1 ] || [ "$UID" = "0" ]; then
        mspti_right=${root_mspti_right}
        right=${root_right}
    else
        mspti_right=${user_mspti_right}
        right=${user_right}
    fi
}

function install_whl_package() {
    local _pylocal=$1
    local _package=$2
    local _pythonlocalpath=$3

    print ${LEVEL_INFO} "Start to install ${_package}."
    if [ ! -f "${_package}" ]; then
        print ${LEVEL_ERROR} "Install whl The ${_package} does not exist."
        exit 1
    fi
    if [ "-${_pylocal}" = "-y" ]; then
        pip3 install --upgrade --no-deps --force-reinstall "${_package}" -t "${_pythonlocalpath}" > /dev/null 2>&1
    else
        if [ "$(id -u)" -ne 0 ]; then
            pip3 install --upgrade --no-deps --force-reinstall "${_package}" --user > /dev/null 2>&1
        else
            pip3 install --upgrade --no-deps --force-reinstall "${_package}" > /dev/null 2>&1
        fi
    fi
    if [ $? -ne 0 ]; then
        print ${LEVEL_ERROR} "Install ${_package} failed."
        exit 1
    fi
    print ${LEVEL_INFO} "Install ${_package} success."
}

function implement_install() {
    create_directory ${install_path}/${MSPTI_INCLUDE_PATH} ${right}
    create_directory ${install_path}/${MSPTI_LIB_PATH} ${right}
    create_directory ${install_path}/${MSPTI_PYTHON_PATH} ${right}
    for header in "${MSPTI_HEADER[@]}"; do
        copy_file ${header} ${install_path}/${MSPTI_INCLUDE_PATH}/${header} ${mspti_right}
    done
    copy_file ${LIBMSPTI} ${install_path}/${MSPTI_LIB_PATH}/${LIBMSPTI} ${mspti_right}
    copy_file ${SAMPLES} ${install_path}/${MSPTI_PATH}/${SAMPLES} ${right}
    local mspti_whl=${install_path}/${MSPTI_PYTHON_PATH}/${MSPTI_WHL}
    copy_file ${MSPTI_WHL} ${mspti_whl} ${right}
    install_whl_package ${pylocal} ${mspti_whl} ${install_path}/python/site-packages
    if [ -d ${install_path}/lib64 ]; then
        cd ${install_path}/lib64
        create_softlink ../../${MSPTI_LIB_PATH}/${LIBMSPTI} ${install_path}/lib64/${LIBMSPTI}
    fi
    if [ -d ${install_path}/include ]; then
        cd ${install_path}/include
        create_softlink ../../${MSPTI_INCLUDE_PATH} ${install_path}/include/mspti
    fi
}

function copy_file() {
    local filename=${1}
    local target_file=$(readlink -f ${2})
    local _right=${3}
    if [ ! -f "${filename}" ] && [ ! -d "${filename}" ]; then
        print ${LEVEL_ERROR} "${filename} does not exist."
        exit 1
    fi
    if [ -f "${target_file}" ] || [ -d "${target_file}" ]; then
        local parent_dir=$(dirname ${target_file})
        local parent_right=$(stat -c '%a' ${parent_dir})
        chmod u+w ${parent_dir}
        chmod -R u+w ${target_file}
        rm -rf ${target_file}
        cp -r ${filename} ${target_file}
        chmod -R ${_right} ${target_file}
        chmod ${parent_right} ${parent_dir}
    else
        cp -r ${filename} ${target_file}
        chmod -R ${_right} ${target_file}
    fi
    print ${LEVEL_INFO} "${filename} is replaced."
}

function create_directory() {
    local _dir=${1}
    local _right=${2}
    if [ ! -d "${_dir}" ]; then
        mkdir -p ${_dir}
        chmod ${_right} ${_dir}
    fi
}

function create_softlink() {
    local _src=$1
    local _dst=$2
    if [ -z "${_src}" ] || [ -z "${_dst}" ]; then
        print ${LEVEL_ERROR} "parameter error"
        exit 1
    fi
    if [ ! -e "${_src}" ]; then
        print ${LEVEL_ERROR} "'${_src}' does not exist"
        exit 1
    fi
    if [ -L "${_dst}" ];then
        return
    fi
    if [ -e "${_dst}" ]; then
        rm -rf ${_dst}
    fi
    ln -sf ${_src} ${_dst}
    if [ ! -L "${_dst}" ]; then
        print ${LEVEL_ERROR} "create softlink '${_dst}' for '${_src}' failed"
        exit 1
    fi
}

source utils.sh

right=${user_right}
arch_name="${package_arch}-linux"
get_right
implement_install

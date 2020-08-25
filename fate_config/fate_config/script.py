#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import click
from fate_config._utils import get_config_path, backup, recover


@click.group(name="config")
def config():
    pass


@config.command(name="edit")
def _edit():
    """
    edit config
    """
    click.edit(filename=get_config_path("service_conf.yaml"))


@config.command(name="backup")
@click.option("--dst", type=click.Path(),
              help="directory to backup configs to")
def _backup(dst):
    """
    backup configs
    """
    backup(dst, names=["base_conf.yaml"])


@config.command(name="recover")
@click.option("--src", type=click.Path(),
              help="directory to recover configs from")
def _recover(src):
    """
    recover configs
    """
    recover(src, names=["service_conf.yaml"])

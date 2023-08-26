# GHCN

This repo sets up a local version of the GHCN historical daily weather (max, min, precipitation) recorded by weather stations around the world.

Please note that while some of the snippets within may be useful in a production environment, this code is meant to be used for demos and experiments, and is not intended to be optimized for high load or scale.

## Local provisioning

Ansible is used to provision a 3-node YugabyteDB database cluster.

The command for provisioning a test cluster is:
`ansible-playbook -i inventory.yml tasks/ghcn.yml`

## Scenarios

After the cluster is running, various scenarios can be run. Current available scenarios are:

- TBD

## Prerequisites

- a copy of yugabytedb (see <https://download.yugabyte.com> for one option)
- set the group_vars yb_executable_dir to point to your desired YugabyteDB version
- set your path to include the bin and postgres/bin folders within your desired YugabyteDB version
- use set_ips.sh to set local ips for 3 nodes via set_ips.sh (127.0.0.1 - 127.0.0.3)
- add public ssh key to ~/.ssh/authorized_users file and ssh-add it
- some of the scenarios assume you've upgraded your bash version to something modern (e.g., 5.2.15)

## Customization

If you need to change gflags for YugabyteDB, add the key/value in groups_vars/all and then in the template at tasks/yugabytedb/templates/[tserver.conf.j2|catalog.conf.j2].

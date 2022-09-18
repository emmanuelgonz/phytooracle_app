#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2022-09-17
Purpose: Web application for launching PhytoOracle data processing pipelines on high performance computing clusters
"""

import argparse
import os
import sys
import streamlit as st
from PIL import Image
import subprocess as sp
from subprocess import Popen, PIPE
# import paramiko
# import getpass
from paramiko import SSHClient

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('r'),
    #                     default=None)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()

def run_command(existing_client, command):

    stdin, stdout, stderr = existing_client.exec_command(command)
    # process = sp.Popen(command_list, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    # stdout, stderr = process.communicate()
    # print(stdout)
    
    return stdin, stdout, stderr

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    cwd = os.getcwd()

    args = get_args()
    # st.write('PhytoOracle | Modular, Scalable Phenomic Data Processing Pipeline')
    st.title('PhytoOracle | Modular, Scalable Phenomic Data Processing Pipeline')
    logo = Image.open('./images/IMG_0102.PNG')
    example = Image.open('./images/lettuce_data_examples.png')
    platform = Image.open('./images/wsj.jpg')

    st.image(logo, use_column_width='always')
    st.image(example, use_column_width='always')
    st.write('PhytoOracle (PO) Automation is general-use, distributed computing pipeline for phenomic \
              data. PO can be run on local or HPC resources and is capable of processing large phenomic \
              datasets such as those collected by the Field Scanner at the University of Arizona\'s Maricopa \
              Agricultural Center (pictured below, Photo: Jesse Rieser for The Wall Street Journal).')
    st.image(platform, use_column_width='always')


    st.write("PO\'s distributed framework, leveraging CCTools\' Makeflow and Workqueue, allows users to leverage \
              hundreds to thousands of computing cores for parallel processing of large data processing tasks. \
             The pipeline is run using a YAML file, which specifies processing steps run by the pipeline.")

    # sp.call('ssh -X emmanuelgonzalez@hpc.arizona.edu && ssh wentletrap.hpc.arizona.edu && ls', shell=True) 
    # data = sp.check_output('ssh -X emmanuelgonzalez@hpc.arizona.edu && ssh wentletrap.hpc.arizona.edu && ls'.split(' '), shell=True) #.call('ls', shell=True)
    # st.write(data)

    # p1 = sp.Popen(["ssh", "emmanuelgonzalez@hpc.arizona.edu"], stdout=sp.PIPE, shell=True)
    # p2 = sp.Popen(["ssh", "wentletrap.hpc.arizona.edu"], stdin=p1.stdout, stdout=sp.PIPE, shell=True)
    # p3 = sp.Popen(["mkdir", "this_is_a_test"], stdin=p2.stdout, stdout=sp.PIPE, shell=True)
    # p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    # p2.stdout.close()
    # output = p3.communicate()[0]
    # st.write(output)

    # p = Popen(['ssh', '"emmanuelgonzalez@hpc.arizona.edu"'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # rc = p.returncode
    # print(output)

    # sp.call('ssh -X emmanuelgonzalez@hpc.arizona.edu', shell=True)
    # sp.call('ssh wentletrap.hpc.arizona.edu', shell=True)
    # sp.call('touch this_is_a_test.sh', shell=True)



    client = SSHClient()
    # client.look_for_keys(True)
    client.load_system_host_keys()
    # client.connect('example.com', username='user')
    # client.close()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.look_for_keys(True)
    # p = getpass.getpass()
    client.connect('hpc.arizona.edu', username='emmanuelgonzalez')
    
    stdin, stdout, stderr = run_command(existing_client=client, command='ls')
    st.write(stdout.readlines())

    client.close()
    

# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env bash

sudo su -c 'sed s/^GRUB_CMDLINE_LINUX_DEFAULT=\"text\"/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\ splash\"/ /etc/default/grub > /etc/default/grub_pending'

sudo su -c 'cat /etc/default/grub_pending > /etc/default/grub && rm /etc/default/grub_pending'

sudo update-grub

echo 'After rebooting, you will now be in graphical mode!'

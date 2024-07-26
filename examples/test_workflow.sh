#!/bin/bash

set -ex

basket maas list
basket maas use deepseek
basket maas reset deepseek
basket maas use deepseek

basket model list
basket model use deepseek-chat

basket config

basket chat "Who are you?"
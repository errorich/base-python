#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import unittest
from unittest.mock import Mock, patch
import lib

class ClassTest(unittest.TestCase):


    def test_server_action(self):

        recv = 'test_hello'
        recv_json = json.dumps(recv)
        recv_buf = recv_json.encode()

        compare_to = 'Сервер получил и обработал следующее сообщение: '\
                     '"test_hello"'

        virt_sock = Mock()
        virt_sock.send.return_value = None
        virt_sock.recv.return_value = recv_buf

        result = lib.server_action(virt_sock)

        self.assertEqual(result, compare_to)

    def test_client_action(self):

        recv = 'Сервер получил и обработал следующее сообщение: "test_hello"'
        recv_json = json.dumps(recv)
        recv_buf = recv_json.encode()

        virt_sock = Mock()
        virt_sock.send.return_value = None
        virt_sock.recv.return_value = recv_buf

        user_input = 'test_hello'

        with patch('builtins.input', side_effect=user_input):
            result = lib.client_action(virt_sock)

        self.assertEqual(result, recv)

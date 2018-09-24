import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cowsay_installed(host):
    p = host.package('cowsay')

    assert p.is_installed


def test_cowsay(host):
    cmd = host.run('cowsay \'hello world!\'')
    expected = (' ______________\n'
                '< hello world! >\n'
                ' --------------\n'
                '        \\   ^__^\n'
                '         \\  (oo)\\_______\n'
                '            (__)\\       )\\/\\\n'
                '                ||----w |\n'
                '                ||     ||')

    assert cmd.rc == 0
    assert expected == cmd.stdout

# Updates for Doing this Demo in 2018

The following updates allow you to run this demo in 2018 from an OS X
10.13.x machine. A video of this demo is on the [AnsibleFest SF 2017](https://www.ansible.com/infrastructure-testing-with-molecule)
website. The original code is from [ehashman/ansiblefest](https://github.com/ehashman/ansiblefest).

## Prerequisites
You will need Vagrant (e.g. `brew install vagrant`) and Python 3
(e.g. `brew install python3`) installed before you can begin.

This demo is done in a python virtualenv. There are a few ways to set this up, but I use
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
It is out of scope to describe how to set up this tool. To create your
virtualenv using wrapper run `mkvirtualenv cowsay`. If you use a
different tool, create your environment before starting.

Once in your empty virtualenv, run `pip install -r requirements` to
install molecule and its dependencies. I also install `python-vagrant`
using pip because of OS X; if you are running on debian or ubuntu you
will probably want to install that using `sudo apt-get install
python-vagrant` (this command might not work on Ubuntu 14.04 trusty).

## 1 - Initialize Your Role

Starting from scratch, run `molecule init role -r cowsay -d vagrant`.

## 2 - Create VM and Do First Check

```
cd cowsay
molecule create
molecule converge
molecule idempotence
molecule verify
```

Note: `molecule verify` produces 9 warnings for me because of a
depreciation of `collections.abc` which is used by a number of modules
that `molecule` is dependent on. The default `/etc/hosts` check passes
as expected.

## 3 - Create Cowsay Task

Edit `tasks/cowsay.yml` and `tasks/main.yml` to install the `cowsay`
package.

## 4 - Check New Tasks for Regression
```
molecule idempotence
molecule verify
```

## 5 - Update test_default.py

Don't test for existence of the package. That's what Ansible does! (I'm
including it though to keep it consistent with the demo.)

Instead, check that `cowsay` works!


Remove the `/etc/hosts` test and add these two tests:

```
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
```


## 6 - Verify From Scratch

```
molecule destroy
# drink some water
molecule test
# note that flake8 v3.5.0 has a error that produces a regex warning
#      see [issue 728](https://github.com/PyCQA/pycodestyle/issues/728)
```

At this point both tests pass!

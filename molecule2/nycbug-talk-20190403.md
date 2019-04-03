# NYC*BUG Talk 2019 April 3

## Who Am I
Raúl Cuza. SysAdmin. Working with Linux at work.

* Excited that FreeBSD is easily installable using Vagrant and EC2 AMIs.

## Overview of Talk

First part is a demo of molecule. I will assume you know what Ansible
is, but will go through my Ansible example module slowly so you can ask
questions.

## Walk Thru Ansible Role
What is Ansible? A DSL and ssh pipe.

What is the `cowsay` role?

What do we need to test?

We will test with `molecule`

## Demo What Molecule Does

Requirements:
* network (otherwise `sudo` doesn't work)
* ansible and molecule installed (ok to use python virtualenv)

Walk through the steps in a clean fashion.

```
workon molecule
molecule create -s freebsd
molecule converege -s freebsd
molecule idempotence -s freebsd
molecule verify -s freebsd
```

## Do Everything At Once

`molecule test --all --destroy never`


pretty cool

## Show Me the Duct Tape

Story: the bug I had to solve to get a BSD instance working
* yaml
* Vagrant config (ruby)
* python
* shell
* ssh
* Differences between Ubuntu and FreeBSD


## What Does Testing Give Us?

Q&A

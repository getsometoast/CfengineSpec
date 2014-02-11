The Dream
============

To have a testing framework for TDDing cf-engine promises as awesome as ChefSpec.

The Reality
===========

This is just a dumping ground for some tests using the --dry-run option of cf-agent to see if it's at all possible to build something like ChefSpec for cf-engine.

Notes
==========
Want the syntax to look something like this:

- Cfengine.should create("/tmp/hello-world.txt")
- Cfengine.should manage_service("mongodb") 
- Cfengine.should create("/var/log/newrelic") with permissions("0700") for user("newrelic")
- Cfengine.should install_package("python-dev")
- Cfengine.should run_command("/usr/bin/lib/pip install newrelic_plugin_agent")

Regarding implementation - could write a promise that outputs generic report statement for promise types like:

- R: PACKAGE: INSTALLED: Installed package ssh.

then, as long as I'm always using this promise, the cf-agent --dry-run output would be simple to parse to make assertions about.


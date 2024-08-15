# how to operate fibrae

[implementation of fabric's](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)

[Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)

[fab docs](https://docs.fabfile.org/en/1.13/usage/fab.html)

[Understanding CI in CD](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/)

CI/CD
The lean/agile methodology (See: Twelve Principles of Agile Software) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

code
ship your code
measure the impact
learn from it
fix or improve it
start over

As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).

applied to software engineering, CI/CD (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

Shipping the code:
  Capistrano, Fabric
Encapsulating the code
  Docker, Packer
Testing the code
  Jenkins, CircleCi, Travis
Measuring the code
  Datadog, Newrelic, Wavefront

  [ngix config](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/)

[Fabric docs](https://www.fabfile.org/)

fab -f 3-deploy_web_static.py deploy
ubuntu
versions/web_static_202481501729.tgz

fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz
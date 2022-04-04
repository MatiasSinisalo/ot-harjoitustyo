from invoke import task
@task
def start(ctx):
    ctx.run("poetry python run src/index.py", pty=True)

@task
def coverage(ctx):
    ctx.run("poetry run coverage run --branch -m pytest src", pty=True)

@task
def coverage_report(ctx):
    ctx.run("poetry coverage html", pty=True)


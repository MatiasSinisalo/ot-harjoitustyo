from invoke import task
@task
def start(ctx):
    ctx.run("poetry run python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("poetry run pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("poetry run coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("poetry coverage html", pty=True)


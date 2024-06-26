import nox


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def tests(session):
    session.install(".")
    session.run("pytest")

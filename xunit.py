class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def testRunning(self):
        print("here")
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("testRunning").run()

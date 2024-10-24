from nbresult import ChallengeResultTestCase


class TestBase_precision(ChallengeResultTestCase):
    def test_precision_score(self):
        self.assertGreater(self.result.score, 0,
                           msg="Score should be positive. Did you choose a regression metric maybe?")
        self.assertGreater(self.result.score, 0.72,
                           msg="Seems you chose the wrong metric.")
        self.assertLess(self.result.score, 0.80,
                           msg="Seems you chose the wrong metric.")

import runner
import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner('Феликс')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = runner.Runner('Игорь')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_chellenge(self):
        runner1 = runner.Runner('Феликс')
        runner2 = runner.Runner('Игорь')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            #print(i)
            final_result = {}
            for key, value in i.items():
                final_result[key] = value.name  #Runner
           #print(final_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tournament_2.start()
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tournament_3.start()
        self.assertTrue(self.all_results[max(self.all_results)] == 'Ник')
        TournamentTest.all_results[3] = self.all_results
        #print(TournamentTest.all_results.keys())


if __name__ == "__main__":
    unittest.main()

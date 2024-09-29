import unittest
import rt_with_exceptions as rt_ex
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='UTF-8',
                        format='||| %(asctime)s ||| %(levelname)s ||| %(module)s ||| %(message)s |||')

class RunnerTest(unittest.TestCase):
    y = False
    @unittest.skipIf(y, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            test_petr = rt_ex.Runner('Petr', -9)
            for _ in range(10):
                test_petr.walk()
            self.assertEqual(test_petr.distance, 90)
            logging.info("'test_walk' выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(y, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            test_petr = rt_ex.Runner(True, 9)
            for _ in range(10):
                test_petr.run()
            self.assertEqual(test_petr.distance, 180)
            logging.info("'test_run' выполнен успешно")
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(y, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        test_petr = rt_ex.Runner('Petr', 9)
        test_vasya = rt_ex.Runner('Vasya', 3)
        for _ in range(10):
            test_petr.run()
            test_vasya.run()
        self.assertNotEqual(test_petr.distance, test_vasya.distance)


if __name__ == '__main__':
    unittest.main()

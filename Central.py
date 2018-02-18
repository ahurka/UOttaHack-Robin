from MultiLevel import FourLevelFeedbackQueue
import Dismissal
from sys import argv


class Stuff:
    def __init__(self, num_doctors):
        self._queue = FourLevelFeedbackQueue(num_doctors)

    def get_priority(self, description):
        if "heavy_bleeding" in description:
            return (0, 30)
        elif "third-degree_burns" in description:
            return (0, 60)
        elif "broken_arm" in description:
            return (2, 25)
        elif "heavy_bruising" in description:
            return (1, 15)
        elif "broken_finger" in description:
            return (1, 20)
        elif "mild_headache" in description:
            return (3, 10)

    def load_data(self, p_key, name, description):

        if p_key not in self._queue:
            stats = self.get_priority(description)

            judge = Dismissal.DeterministicDismissalGenerator()
            self._queue.add_item(p_key, name, stats[1], stats[0])
            if judge.judge_dismissal(stats[0], self._queue.get_expected_time(p_key)):
                self._queue.cancel(p_key)
                return tuple([name, judge.get_dismissal_string()])
        time = self._queue.get_expected_time(p_key)
        return tuple([name, time])

    def get_delay(self, p_key):
        return self._queue.get_expected_time(p_key)

    def schedule_next(self):
        return self._queue.schedule_next()

    def conclude(self, p_key):
        return self._queue.finish_op(p_key)


if __name__ == "__main__":
    system = Stuff(1)

    while (1):
        blab = input()
        str = blab.split(" ")
        if str[0] == "enter":
            print(system.load_data(str[1], str[2], str[3]))
        elif str[0] == "check":
            print(system.get_delay(str[1]))
        elif str[0] == "start":
            print(system.schedule_next())
        elif str[0] == "finish":
            print(system.conclude(str[1]))


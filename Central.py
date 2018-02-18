from MultiLevel import FourLevelFeedbackQueue
import Dismissal


class Stuff:
    def __init__(self, num_doctors):
        self._queue = FourLevelFeedbackQueue(num_doctors)

    def get_priority(self, description):
        if "heavy bleeding" in description:
            return (0, 30)
        elif "third-degree burns" in description:
            return (0, 60)
        elif "mild headache" in description:
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

class DismissalGenerator:
    def judge_dismissal(self, critical_code, minutes):
        raise NotImplementedError

    def get_dismissal_string(self):
        return "Due to your long projected waiting time and the non-critical" \
               " nature of your diagnosis, we recommend resting and recovering" \
               " at home. Thank you for coming to Walk-In Clinic #52578."


class DeterministicDismissalGenerator(DismissalGenerator):
    def judge_dismissal(self, critical_code, minutes):
        if critical_code == 3:
            return minutes > 60
        elif critical_code == 2:
            return minutes > 120
        elif critical_code == 1:
            return minutes > 240
        else:
            return False

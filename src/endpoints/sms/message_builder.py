# helper class for message templates

class MessageBuilder:
    welcome = "From Children's National:\n"
    optout = "Reply 'STOP' to opt-out of texts.\n"

    def careteam_message(self, full_name, role):
        msg = self.welcome + "{}{} has been added to your active CareTeam\n".format(full_name, role) + self.optout
        return msg

    def encounter_move_message(self, location):
        msg = self.welcome + "Patient has been moved to {}\n".format(location) + self.optout
        return msg

    def nutrition_message(self, item, time):
        msg = self.welcome + "Patient received {} at {}\n".format(item, time) +  self.optout
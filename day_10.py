import pydot
import re

with open("input_day_10.txt") as f:
    code = f.readlines()

#code = ["value 5 goes to bot 2", "bot 2 gives low to bot 1 and high to bot 0", "value 3 goes to bot 1", "bot 1 gives low to output 1 and high to bot 0", "bot 0 gives low to output 2 and high to output 0", "value 2 goes to bot 2"]
#code = ["value 5 goes to bot 2", "value 2 goes to bot 2", "value 3 goes to bot 1", "bot 2 gives low to bot 1 and high to bot 0", "bot 1 gives low to output 1 and high to bot 0", "bot 0 gives low to output 2 and high to output 0" ]

class Robot:

    graph = None
    bot_dict = {}

    def __init__(self):
        self.graph = pydot.Dot(graph_type='digraph')
        pass

    def parse(self, code):
        for instruct in code:
            if instruct.split(" ", 1)[0] == "value":
                m = re.match("value (\d+) goes to bot (\d+)", instruct)
                value = int(m.group(1))
                bot_id =  int(m.group(2))
                edge = pydot.Edge("value %d" % value, "bot %d" % bot_id)
                self.graph.add_edge(edge)
                self.update_bot_input(bot_id, value)
            elif instruct.split(" ", 1)[0] == "bot":
                m = re.match("bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", instruct)
                bot_id = int(m.group(1))
                sink_low = "%s %d" % (str(m.group(2)), int(m.group(3)))
                sink_high = "%s %d" % (str(m.group(4)), int(m.group(5)))
                edge_low = pydot.Edge("bot %d" % bot_id, sink_low, color='blue')
                edge_high = pydot.Edge("bot %d" % bot_id, sink_high, color='red')
                self.graph.add_edge(edge_low)
                self.graph.add_edge(edge_high)
                if not self.bot_exist(bot_id):
                    self.add_bot(bot_id)
                if self.bot_dict[bot_id].sink_low is None and self.bot_dict[bot_id].sink_high is None:
                    self.bot_dict[bot_id].sink_low = sink_low
                    if sink_low.split(" ")[0] == "bot":
                        self.update_bot_source(sink_low.split(" ")[1], "bot %d"%bot_id)

                    self.bot_dict[bot_id].sink_high = sink_high
                    if sink_high.split(" ")[0] == "bot":
                        self.update_bot_source(sink_high.split(" ")[1], "bot %d"%bot_id)

                if isinstance(self.bot_dict[bot_id].input_value_a, int) and isinstance(self.bot_dict[bot_id].input_value_b, int):
                    if sink_low.split(" ")[0] == "bot":
                        self.update_bot_input(int(sink_low.split(" ")[1]), min(self.bot_dict[bot_id].input_value_a,
                                                          self.bot_dict[bot_id].input_value_b))
                    if sink_high.split(" ")[0] == "bot":
                        self.update_bot_input(int(sink_high.split(" ")[1]), max(self.bot_dict[bot_id].input_value_a,
                                                          self.bot_dict[bot_id].input_value_b))



    def update_bot_input(self, bot_id, value):
        if not self.bot_exist(bot_id):
            self.add_bot(bot_id)
        self.bot_add_value(bot_id, value)


    def bot_exist(self, bot_id):
        if int(bot_id) in self.bot_dict.keys():
            return True
        else:
            return False

    def bot_add_value(self, bot_id, value):
        if self.bot_dict[bot_id].input_value_a is None:
            self.bot_dict[bot_id].input_value_a = int(value)
        elif isinstance(self.bot_dict[bot_id].input_value_a, int) and self.bot_dict[bot_id].input_value_b is None:
            self.bot_dict[bot_id].input_value_b = int(value)
            if self.bot_dict[bot_id].sink_low is not None:
                if self.bot_dict[bot_id].sink_low.split(" ")[0] == "bot":
                    self.update_bot_input(int(self.bot_dict[bot_id].sink_low.split(" ")[1]), min(self.bot_dict[bot_id].input_value_a,
                                                                           self.bot_dict[bot_id].input_value_b))
                if self.bot_dict[bot_id].sink_high.split(" ")[0] == "bot":
                    self.update_bot_input(int(self.bot_dict[bot_id].sink_high.split(" ")[1]), max(self.bot_dict[bot_id].input_value_a,
                                                                            self.bot_dict[bot_id].input_value_b))
        else:
            print "Error: bot_add_value"
            exit()

    def update_bot_source(self, bot_id, source):
        if not self.bot_exist(bot_id):
            self.add_bot(bot_id)
        self.bot_add_source(bot_id, source)

    def bot_add_source(self, bot_id, value):
        if self.bot_dict[int(bot_id)].source_a is None:
            self.bot_dict[int(bot_id)].source_a = str(value)
        elif isinstance(self.bot_dict[int(bot_id)].source_a, str) and self.bot_dict[int(bot_id)].source_b is None:
            self.bot_dict[int(bot_id)].source_b = str(value)

            if isinstance(self.bot_dict[int(bot_id)].input_value_a, int) and isinstance(self.bot_dict[int(bot_id)].input_value_b, int):
                print "Hit\n\n"
                if self.bot_value_output(bot_id, self.bot_dict[int(bot_id)].source_a):
                    self.update_bot_input(self.bot_dict[int(bot_id)].source_a.split(" ")[1],
                                          self.bot_value_output(bot_id, self.bot_dict[int(bot_id)].source_a))

                if self.bot_value_output(bot_id, self.bot_dict[int(bot_id)].source_b):
                    self.update_bot_input(self.bot_dict[int(bot_id)].source_b.split(" ")[1],
                                          self.bot_value_output(bot_id, self.bot_dict[int(bot_id)].source_b))


        else:
            print "Error: bot_add_value"
            #exit()

    def bot_value_output(self, source_bot_id, sink_bot_id):
        if self.bot_exist(int(source_bot_id)) and self.bot_exist(int(sink_bot_id)):
            if "bot %d"%int(sink_bot_id) == self.bot_sink_list(int(source_bot_id))[0]:
                return min(self.bot_dict[int(source_bot_id)].input_a,
                           self.bot_dict[int(source_bot_id)].input_b)
            elif "bot %d"%int(sink_bot_id) == self.bot_sink_list(int(source_bot_id))[1]:
                return max(self.bot_dict[int(source_bot_id)].input_a,
                           self.bot_dict[int(source_bot_id)].input_b)
            else:
                return False
        else:
            return False



    def add_bot(self, bot_id):
        new_bot = Bot()
        new_bot.id = int(bot_id)
        self.bot_dict[int(bot_id)] = new_bot

    def bot_sink_list(self, bot_id):
        if self.bot_exist(int(bot_id)):
            if self.bot_dict[int(bot_id)].sink_low is not None: # assume sinks are always provided
                return self.bot_dict[int(bot_id)].sink_low, self.bot_dict[int(bot_id)].sink_high
            else:
                return False
        else:
            return False


    def writeGraph(self):
        self.graph.write_png('day_10_graph.png')




class Bot:
    id = None
    input_value_a = None
    input_value_b = None
    output_value_a = None
    output_value_b = None

    source_a = None
    source_b = None

    sink_low = None
    sink_high = None


    def output(self):
        print "ID: %s\tInput A: %s\tInput B: %s\t" \
              "Source A: %s  \tSource B: %s     \t" \
              "Sink Low: %s    \tSink High: %s" % (self.id, self.input_value_a, self.input_value_b, self.source_a, self.source_b, self.sink_low, self.sink_high)

robot = Robot()
robot.parse(code)
robot.writeGraph()

#for key, bot in robot.bot_dict.iteritems():
#    bot.output()

for key, bot in robot.bot_dict.iteritems():
    if (bot.input_value_a == 17 and bot.input_value_b == 61) or \
        (bot.input_value_b == 17 and bot.input_value_a == 61):
        bot.output()


for key, bot in robot.bot_dict.iteritems():
    if (bot.sink_low == "output 0" or bot.sink_high == "output 0") or \
            (bot.sink_low == "output 1" or bot.sink_high == "output 1") or \
            (bot.sink_low == "output 2" or bot.sink_high == "output 2"):
        bot.output()

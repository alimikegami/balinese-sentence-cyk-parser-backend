class ContextFreeGrammar():
    def __init__(self):
        self.rules = self.get_rules()

    def get_rules(self):
        with open("D:\\TUGAS KULIAH\\TBO\\balinese-sentence-cyk-parser-be\\cfg_rules.txt") as cfg:
            lines = cfg.readlines()
        return [x.replace("->", "").split() for x in lines]

class CYK():
    def __init__(self, sentence, cfg):
        self.cfg = cfg.rules
        self.sentence = sentence.split()
        self.tree = []
        self.length= len(self.sentence)
        self.table = [[[] for x in range(self.length - y)] for y in range(self.length)]

    def check_word_in_rules(self, word, term):
        x = "'" + word + "'"
        if (x == term):
            return True
        return False

    def parse(self):
        # Simpan seluruh non-terminal yang dapat men-generate
        # terminal kalimat pada tabel
        for i in range(0, self.length):
            for rule in self.cfg:
                if (self.check_word_in_rules(self.sentence[i], rule[1])):
                    self.table[0][i].append(Production(rule[0], self.sentence[i]))
        
        for num_of_words in range(2, self.length + 1):
            for j in range(0, self.length - num_of_words + 1):
                for left_size in range(1, num_of_words):
                    left_cell = self.table[left_size - 1][j]
                    right_cell = self.table[(num_of_words - left_size) - 1][j + left_size]
                    for rule in self.cfg:
                        first_non_terms = []
                        for prod in left_cell:
                            if prod.non_terminal == rule[1]:
                                first_non_terms.append(prod)
                        if first_non_terms:
                            second_non_terms = []
                            for prod in right_cell:
                                if prod.non_terminal == rule[2]:
                                    second_non_terms.append(prod)
                            for non_term_1 in first_non_terms:
                                for non_term_2 in second_non_terms:
                                    self.table[num_of_words - 1][j].extend([Production(rule[0], non_term_1, non_term_2)])
        flag = False
        for non_term in self.table[-1][0]:
            if non_term.non_terminal == self.cfg[0][0]:
                self.tree.append(self.show_tree(non_term))
                flag = True
        return flag

    def show_tree(self, prod):
        if prod.terminal_2:
            return {f'{prod.non_terminal}': [self.show_tree(prod.terminal_1), self.show_tree(prod.terminal_2)]}
        
        return {f'{prod.non_terminal}': f'{prod.terminal_1}'}

class Production():
    def __init__(self, non_terminal, terminal_1, terminal_2=None):
        self.non_terminal = non_terminal
        self.terminal_1 = terminal_1
        self.terminal_2 = terminal_2
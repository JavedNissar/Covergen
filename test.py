import unittest
import parser

def fetch_names_table_and_text_lines(file_path):
    cover_letter_template = open(file_path)
    import_lines, text_lines = parser.get_lines(cover_letter_template)
    cover_letter_template.close()

    #get the mapping of names from the import lines
    names_table = parser.parse_import_lines(import_lines)
    return names_table,text_lines

class SampleCoverLetterTest(unittest.TestCase):
    def test_sample(self):
        #get the mapping of names from the import lines
        names_table,text_lines = fetch_names_table_and_text_lines("example/test.coverletter")
        self.assertEqual(names_table['java'],('programming.languages.java',1))

        #get the mapping of names to libraries from the import_lines
        library_table = parser.get_dictionaries(names_table,'example')
        self.assertEqual(library_table['java']['highschool'],"I completed two programming courses in Java when I was in high school")

        #compile the text lines using the libraries from earlier
        text = parser.parse_text_lines(text_lines, library_table)

        with open("example/test.coverletter.output.gold") as correct_output_file:
            correct_output = correct_output_file.read()
            self.assertEqual(text,correct_output)

    def test_sample2(self):
        names_table,text_lines = fetch_names_table_and_text_lines("example/test2.coverletter")
        self.assertEqual(names_table['java'],('programming.languages.java',2))
        self.assertEqual(names_table['javascript'],('programming.languages.javascript',3))
        self.assertEqual(names_table['go'],('programming.languages.go',1))

        library_table = parser.get_dictionaries(names_table,'example')
        self.assertEqual(library_table['java']['highschool'],"I completed two programming courses in Java when I was in high school")
        self.assertEqual(library_table['javascript']['clearlifegoals'],"I built a website for helping users manage their goals using Jquery and Cytoscape.js")
        self.assertEqual(library_table['javascript']['autotweet'],"I built a utility for automatically generating tweets using Markov Chains")
        self.assertEqual(library_table['go']['clearlifegoals'],"designed a web application that encrypts user data using the Nacl cryptographic library")

        text = parser.parse_text_lines(text_lines, library_table)

        with open("example/test2.coverletter.output.gold") as correct_output_file:
            correct_output = correct_output_file.read()
            self.assertEqual(text,correct_output)

if __name__ == '__main__':
    unittest.main()

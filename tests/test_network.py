"""
Test module for the network class
"""
import unittest
import phievo

class mock_interaction(phievo.Networks.classes_eds2.Interaction):
    def __init__(self,list_input,output,net):
        
        net.add_Node(self)
        net.add_Node(output)
        for input in list_input:
            net.graph.add_edge(input,self)
        net.graph.add_edge(self,output)

class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.net = phievo.Networks.classes_eds2.Network()

    def test_add_Node(self):
        self.species1 = phievo.Networks.classes_eds2.Species([['Degradable',0.1]])
        self.assertTrue(self.net.add_Node(self.species1))
        self.assertFalse(self.net.add_Node(self.species1))
        self.assertIn(self.species1,self.net.nodes())

    def test_new_Species(self):
        self.spc = self.net.new_Species([['Degradable',0.1]])
        self.assertIn(self.spc,self.net.nodes())

    def test_number_nodes(self):
        self.net.dict_types = dict(a=[1,1],b=[]) #dummy list_types
        self.assertEqual(self.net.number_nodes('a'),2)
        self.assertEqual(self.net.number_nodes('b'),0)
        self.assertEqual(self.net.number_nodes('c'),0)

    def test_check_existing_binary(self):
        self.s1 = self.net.new_Species([['Input',0]])
        self.s2 = self.net.new_Species([['Input',1]])
        self.s3 = self.net.new_Species([['Output',0]])
        self.inter = mock_interaction([self.s1,self.s2],self.s3,self.net)
        self.inter = mock_interaction([self.s2],self.s3,self.net)
        
        ceb = self.net.check_existing_binary
        self.assertTrue(ceb([self.s1,self.s2],'Interaction'))
        self.assertTrue(ceb([self.s1,self.s2],'mock_interaction'))
        self.assertFalse(ceb([self.s1,self.s3],'mock_interaction'))
        self.assertFalse(ceb([self.s1],'mock_interaction'))
        self.assertTrue(ceb([self.s2],'Interaction'))
        

if __name__ == '__main__':
    unittest.main()

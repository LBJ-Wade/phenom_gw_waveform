
class Waveform(object):
    """docstring for Waveform
    p : dict
        dictionary of physical parameters:
        'mass1', 'mass2',
        'spin1x', 'spin1y', 'spin1z',
        'spin2x', 'spin2y', 'spin2z',
        'f_min', ,'f_max' 'delta_f',
        'theta_LN',
        'tc', 'phic', 'ra', 'dec', 'polarization',
        'approximant',
        'detectors'
        """
    def __init__(self, p):
        """p is actually a kwargs but is used in classes like PhenomD"""
        self.p = p
        # TODO: set default values for p
        if 'f_max' not in p.keys():
            self.p['f_max'] = 0

    def waveform_method(self):
        print "I am from Waveform"
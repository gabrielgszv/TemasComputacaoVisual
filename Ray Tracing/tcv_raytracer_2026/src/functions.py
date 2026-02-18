#============================================
# Funções da tarefa
#============================================

def heart_function(x, y, z):
    return (x*x + 9/4*y*y + z*z -1)**3 \
        - x*x*z*z*z \
        - 9/80*y*y*z*z*z

def mitchel_function(x, y, z):
    return 4*(x**4 + (y*y + z*z)**2) \
        + 17*x*x*(y*y + z*z) \
        - 20*(x*x + y*y + z*z) \
        + 17

#============================================
# Funções do site
#============================================

def calyx_function(x, y, z):
    return x**2 + y**2 - z**4


def calypso_function(x, y, z):
    return x**2 + y**2 - z**2


def columpius_function(x, y, z):
    return x**3*y + x*z**3 + y*z**3 + z**7 + 5*z


def dattel_function(x, y, z):
    return 3*x**2 + 3*y**2 + z**2 - 1


def daisy_function(x, y, z):
    return (x**2 - y**3)**2 - (z**2 - y**3)**3


def dingdong_function(x, y, z):
    return x**2 + y**2 + z**3 - z**2


def durchblick_function(x, y, z):
    return x**3*y + x*z**3 + y**3*z + z**3 + 5*z


def eistute_function(x, y, z):
    return (x**2 + y**2)**3 - 4*x**2*y**2*(z**2 + 1)


def eve_function(x, y, z):
    return 5*x**2 + 2*x*z**2 + 5*y**6 + 15*y**4 + 5*z**2 - 15*y**5 + 5*y**3


def geisha_function(x, y, z):
    return x**2*y*z + x**2*z**2 - y**3*z + y**3


def harlekin_function(x, y, z):
    return x**3*z + 10*x**2*y + x*y**2 + y*z - z**3


def helix_function(x, y, z):
    return 6*x**2 - 2*x**4 - y*z**2


def himmel_und_holle_function(x, y, z):
    return x**2 - y**2*z**2


def kolibri_function(x, y, z):
    return x**3 + x*z**2 - y**2


def leopold_function(x, y, z):
    return x**2*y*z**2 + 3*x**2 + 3*y**2 + z**2 - 1


def plop_function(x, y, z):
    return x**2 + (z + y**2)**3


def seepferdchen_function(x, y, z):
    return (x**2 - y**3)**2 - (x + y**2)*z**3


def sofa_function(x, y, z):
    return x**2 + y**3 + z**3


def suss_function(x, y, z):
    return (x**2 + (9/4)*y**2 + z**2 - 1)**3 - x**2*z**3 - (9/80)*y**2*z**3


def tanz_function(x, y, z):
    return y**4 - x**2 - y**2*z


def taube_function(x, y, z):
    return 256*z**3 - 128*x**2 + 16*x**4 - 144*x*y**2 - 4*x**3*y - 27*y**4


def spitz_function(x, y, z):
    return (y**2 - x**2 - z**2)**3 - 27*x**2*z**2


def tobel_function(x, y, z):
    return x**3*z + x**2 + y*z**3 + z**4 - 3*x*y*z


def vis_a_vis_function(x, y, z):
    return x**2 - x**3 + y**4 + z**3 - z**4


def windkanal_function(x, y, z):
    return -x**2 - y**4 - z**4 - x*y*z - 100


def xano_function(x, y, z):
    return x**4 + z**3 - y*z**2


def zitrus_function(x, y, z):
    return x**2 + z**2 - y**3*(y - 1)**3


def dromedar_function(x, y, z):
    return x**4 - 3*x**2 + y**2*z**3


def zeppelin_function(x, y, z):
    return x*y*z + y*z + 2*z**5


def zweiloch_function(x, y, z):
    return x*y*z + y*z + 2*z**5


def stern_function(x, y, z):
    return x**2*y**2 + y**2*z**2 + z**2*x**2 + 100*(x**2 + y**2 + z**2 - 1)**3

'''
def mobius_function(x, y, z):
    return None
'''

def sphare_function(x, y, z):
    return x**2 + y**2 + z**2 - 1


def torus_function(x, y, z, R=1.0, r=0.3):
    return (x**2 + y**2 + z**2 + R**2 - r**2)**2 - 4*R**2*(x**2 + y**2)


def whitney_function(x, y, z):
    return x**2 - y*z


def buggle_function(x, y, z):
    return x**4*y**2 + x**2*y**4 - x**2*y**2 + z**6


def diabolo_function(x, y, z):
    return x**2 - (y**2 + z**2)


def dullo_function(x, y, z):
    return (x**2 + y**2 + z**2)**2 - (x**2 + y**2)


def miau_function(x, y, z):
    return x**2*y*z + x*z**2 + 2*y**3*z + 3*y**3


def nepali_function(x, y, z):
    return (x*y - z**2 - 1)**2 + (x**2 + y**2 - 1)**3


def pilzchen_function(x, y, z):
    return (z**2 - 1)**2 + (x**2 + y**2 - 1)**3


def subway_function(x, y, z):
    return x**2*y**2 - (z**2 - 1)**3


def crixxi_function(x, y, z):
    return (y**2 + z**2 - 1)**2 + (x**2 + y**2 - 1)**3


def berg_function(x, y, z):
    return x**2 + y**2 + z**3


def gupf_function(x, y, z):
    return x**2 + y**2 + z


def wigwam_function(x, y, z):
    return x**2 + y**2*z**3


def tuelle_function(x, y, z):
    return y*z*(x**2 + y*z)


def pipe_function(x, y, z):
    return x**2 - z


def kreuz_function(x, y, z):
    return x*y*z


def spindel_function(x, y, z):
    return x**2 + y**2 - z**2


def twilight_function(x, y, z):
    return (z**2 - 2)**2 + (x**2 + y**2 - 3)**3

'''
def wendel_function(x, y, z):
    return None
'''

def zeck_function(x, y, z):
    return x**2 + y**2 - z**3*(1 - z)


def sattel_function(x, y, z):
    return x**2 - y**2 + z**3


def cylinder_function(x, y, z):
    return x**2 + y**2 - 1

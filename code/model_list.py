from models.s2i_tune import S2ITune
from models.s2i_spos_search import S2ISPOSSearch
from models.s2i_darts import S2IDartsSearch
MODEL = {
    "S2ITune": S2ITune,
    "S2ISPOSSearch": S2ISPOSSearch,
    "S2IDartsSearch": S2IDartsSearch
}

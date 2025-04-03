from models.base_model import BaseModel
from models.e_s2i_spos_search import ES2ISPOSSearch


class S2ISPOSSearch(BaseModel):
    def __init__(self, args, data, device, s2o, node_wise_feature, batch_pair_num):
        super(S2ISPOSSearch, self).__init__(args, data, device)
        self.ent_encoder = ES2ISPOSSearch(self.args, self.args.embed_size, self.args.hidden_size,
                                           self.args.embed_size,
                                           self.num_rels, s2o, node_wise_feature, batch_pair_num)

from models.base_model import BaseModel
from models.e_s2i_tune import ES2ITune


class S2ITune(BaseModel):
    def __init__(self, args, dataset_info_dict, device, genotype, s2o, node_wise_feature, batch_pair_num):
        super(S2ITune, self).__init__(args, dataset_info_dict, device)
        self.ent_encoder = ES2ITune(genotype, self.args, self.args.embed_size, self.args.hidden_size,
                                              self.args.embed_size,
                                              self.num_rels, s2o, node_wise_feature,batch_pair_num)
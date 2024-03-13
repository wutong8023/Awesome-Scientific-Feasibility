"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "wutong8023"  # github id
author_info = "Tongtong Wu"  # used in introduction
personal_link = "https://wutong8023.site"  # used in introduction
repo_name = "Awesome-Scientific-Feasibility"  # repository name
branch_name = "blob/master"  # branch name
your_research_topic = "SciFy"  # used for dictionary name
your_research_topic_full_name = "Scientific Feasibility (SciFy)"  # used for title
bib_link_overleaf = "https://www.overleaf.com/read/rgscdxhxbwhp"  # used for overleaf
color = "blue"

base_link = f"https://github.com/{user_id}/{repo_name}/{branch_name}/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV", "SIGIR", "SIGKDD", "SIGMOD", "SIGCOMM",
                   "LOUHI@EACL",
                   ],

    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-Based Systems", "Knowl. Based Syst."],
        ["Psychological review", "Psychological Review", "Psychological Review"],
        ["Psychonomic Bulletin and Review", "Psychonomic Bulletin and Review", "Psychonomic Bulletin and Review"],
        ["The Oxford Handbook of Thinking and Reasoning", "The Oxford Handbook of Thinking and Reasoning", "The Oxford Handbook of Thinking and Reasoning",]],

    "Preprint": ["arXiv", "CoRR"],

    # 1: Resource type
    "Contribution": ["Survey", "Empirical Study", "Theory", "Method", "Resource", "Thesis", "Library",
                     "Technical Report", "Other Type"],

    # 2: Application
    "Application Area": ["Material Science", "Artificial Intelligence", "Quantum Computing", "Biomedical", "Other Area"],

    # 3: Research Question
    "RQs": {"Multi-Agent Cooperation",
            "Inductive Reasoning",
            "Counterfactual Reasoning",
            "Temporal Reasoning",
            "First-Order Logic",
            "Inductive Logic Programming",
            "Neural Logic Networks",
            "Others RQs"},

    # 4: Backbone Model
    "Foundation Model": ["ChatGPT", "LLaMA", "T5", "Other Model"],

    # 5: Dataset Format
    "Dataset Format": ["Multi-choice Classification",
                       "Binary Classification",
                       "Other Data Format"
                       ],

}

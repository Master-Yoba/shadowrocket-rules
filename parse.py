import json
import os
import datetime


singbox_to_shadowrocket_mapping = {
    'domain': 'DOMAIN',
    'domain_suffix': 'DOMAIN-SUFFIX',
    'domain_regex': 'URL-REGEX',
    'domain_keyword': 'DOMAIN-KEYWORD',
    'ip_cidr': 'IP-CIDR'
}
source_directory = "singbox-rules"
target_directory = "shadowrocket-rules"
SINGBOX_BINARY_PATH = "./singbox_binary/sing-box"


def singbox_ruleset_to_json(source_file): 
    os.system(f"{SINGBOX_BINARY_PATH} rule-set decompile {source_directory}/{source_file}.srs")  

    with open(f"{source_directory}/{source_file}.json") as f:
        ruleset = json.load(f)

    return(ruleset)


def parse_ruleset(ruleset):
    header_totals = ""
    config = ""
    total_count = 0

    for item in ruleset['rules']:
        for rule_type in item.keys():
            # print(rule_type)
            if isinstance(item[rule_type], str):
                header_totals += f"# {singbox_to_shadowrocket_mapping[rule_type]}: 1\n"
                total_count += 1
                config += f"{singbox_to_shadowrocket_mapping[rule_type]},{item[rule_type]}\n"
            if isinstance(item[rule_type], list):
                header_totals += f"# {singbox_to_shadowrocket_mapping[rule_type]}: {len(item[rule_type])}\n"
                total_count += len(item[rule_type])
                for element in item[rule_type]:
                    config += f"{singbox_to_shadowrocket_mapping[rule_type]},{element}\n"
        header_totals += f"# TOTAL: {total_count}\n"

    return(header_totals, config)


if not os.path.exists(source_directory):
    print("Source dir not found!")
    print("Please create:", source_directory)
    quit()

if not os.path.exists(SINGBOX_BINARY_PATH):
    print("Sing-box binary not found!")
    print("Please put Sing-box binary into:", SINGBOX_BINARY_PATH)
    quit()


files = [f for f in os.listdir(f'./{source_directory}') if '.srs' in f]

if len(files) < 1:
    print("No files to parse!")
    print("Please put .srs files into:", source_directory)
    quit()

if not os.path.exists(target_directory):
    os.makedirs(target_directory)


for source_file in files:
    source_file = source_file[:-4]
    name = source_file#.replace("geosite-", "")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header =  f'''# NAME: {name}
# UPDATED: {timestamp}
'''

    ruleset = singbox_ruleset_to_json(source_file)
    print('parsed', source_file)

    shadowrocket_config_result = header

    header_totals, config = parse_ruleset(ruleset)

    shadowrocket_config_result += header_totals + config
    #print(shadowrocket_config_result)

    with open(os.path.join(target_directory, f"{source_file}.list"), 'w') as f:
        f.write(shadowrocket_config_result)

print('total parsed:', len(os.listdir(target_directory)), 'files')

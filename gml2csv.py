import json
import pandas as pd
from pandas.io.json import json_normalize


def process_gml(file):
    """
    Parser which process the GML file and converts it to JSON objects
    :param file: gml file
    :return: JSON converted from GML
    """

    lines = []
    for line in file.split('\n'):
        line = line.strip()
        lines.append(line)
    file = "\n".join(lines)


    file = file.replace('\n\n', '\n')
    file = file.replace(']\n', '},\n')
    file = file.replace('[\n', '{')
    file = file.replace('\n{', '\n    {')

    for s in ['id', 'label', 'source', 'target', 'value','Country','Longitude','Internal','Latitude','LinkLabel','type']:
        file = file.replace(s, '"%s" :' % s)
    file = file.replace('\n"', ', "')
    file = file.replace('\n}', '}')
    return file.strip('\n')

if __name__ == '__main__':

    # replace the sample file here with your gml file
    graphfile = "sample.gml"

    with open(graphfile, 'r') as f:
        file = f.read()
    file = ''.join(file.split('node')[1:])

    nodes = file.split('edge')[0]

    edges = ''.join(file.split('edge')[1:]).strip().rstrip(']')

    nodes = process_gml(nodes)
    edges = process_gml(edges)

    edges = edges.rstrip(",")
    nodes = nodes.rstrip(",")

    converted_json = "{\"node\":[" + nodes + "],\n" + "\"edges\":[" + edges + "]}"

    data = json.loads(converted_json)

    # converting the node data and edges into dataframes

    df1 = pd.DataFrame.from_dict(json_normalize(data['node']), orient='columns')
    df2 = pd.DataFrame.from_dict(json_normalize(data['edges']),orient='columns')

    # for the column headers
    final_columns = []

    # populate with column names from both data frames
    for col_name in df1.columns:
        final_columns.append(col_name)
    for col_name in df2.columns:
        final_columns.append(col_name)

    # combine both dataframes
    final = pd.concat([df1,df2], ignore_index=True, axis=1)

    # final converted csv
    final.to_csv("final.csv", index=False,header=final_columns)

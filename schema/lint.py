
import os
import glob
import yamale


def validate_all(schema, pattern):
    schema = yamale.make_schema(schema)
    for defs in glob.glob(pattern):
        print (defs)
        data = yamale.make_data(defs)
        yamale.validate(schema, data)
    
if __name__ == '__main__':
    validate_all("./tags.schema.yaml", "../data/*tags*.yaml")
    validate_all("./point.schema.yaml", "../data/*/*point*.yaml")

    

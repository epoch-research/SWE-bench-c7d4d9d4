from swebench.harness import prepare_images
import datasets
import argparse

to_build = [
"django__django-13371",
"django__django-13410",
"django__django-13413",
"django__django-13417",
"django__django-13426",
"django__django-13431",
"django__django-13447",
"django__django-13448",
"django__django-13449",
"django__django-13454",
"django__django-13458",
"django__django-13460",
"django__django-13466",
"django__django-13490",
"django__django-13495",
"django__django-13516",
"django__django-13528",
"django__django-13530",
"django__django-13551",
"django__django-13553",
"django__django-14282",
"django__django-14309",
"django__django-14311",
"django__django-14324",
"django__django-14336",
"django__django-14349",
"django__django-14351",
"django__django-14372",
"django__django-14385",
"django__django-14395",
"django__django-14396",
"django__django-14407",
"django__django-14416",
"django__django-14430",
"django__django-14434",
"django__django-14441",
"django__django-15277",
"django__django-15280",
"django__django-15292",
"django__django-15297",
"django__django-15320",
"django__django-15334",
"django__django-15342",
"django__django-15352",
"django__django-15368",
"django__django-15370",
"django__django-15380",
"django__django-15382",
"django__django-15388",
"django__django-15401",
"django__django-15414",
"django__django-16302",
"django__django-16306",
"django__django-16311",
"django__django-16317",
"django__django-16322",
"django__django-16333",
"django__django-16369",
"django__django-16379",
"django__django-16398",
"django__django-16400",
"django__django-16408",
"django__django-16411",
"django__django-16429",
"django__django-16454",
"django__django-16485",
"django__django-16491",
"django__django-16493",
"django__django-16517",
"django__django-8326",
"matplotlib__matplotlib-19743",
"matplotlib__matplotlib-19763",
"matplotlib__matplotlib-20470",
"matplotlib__matplotlib-21042",
"matplotlib__matplotlib-21238",
"matplotlib__matplotlib-21318",
"matplotlib__matplotlib-21443",
"matplotlib__matplotlib-21481",
"matplotlib__matplotlib-21490",
"matplotlib__matplotlib-21542",
"matplotlib__matplotlib-21550",
"matplotlib__matplotlib-21559",
"matplotlib__matplotlib-21570",
"matplotlib__matplotlib-21617",
"matplotlib__matplotlib-22711",
"matplotlib__matplotlib-22871",
"matplotlib__matplotlib-22926",
"matplotlib__matplotlib-23088",
"matplotlib__matplotlib-23111",
"matplotlib__matplotlib-23266",
"matplotlib__matplotlib-23913",
"matplotlib__matplotlib-24189",
"matplotlib__matplotlib-24224",
"matplotlib__matplotlib-24971",
"matplotlib__matplotlib-25027",
"matplotlib__matplotlib-25052",
"matplotlib__matplotlib-25079",
"matplotlib__matplotlib-25085",
"matplotlib__matplotlib-25129",
"matplotlib__matplotlib-25238",
"matplotlib__matplotlib-25281",
"matplotlib__matplotlib-25287",
"matplotlib__matplotlib-25311",
"matplotlib__matplotlib-25332",
"matplotlib__matplotlib-25334",
"matplotlib__matplotlib-25340",
"matplotlib__matplotlib-25346",
"matplotlib__matplotlib-25404",
"matplotlib__matplotlib-25405",
"matplotlib__matplotlib-25425",
"matplotlib__matplotlib-25551",
"matplotlib__matplotlib-26101",
"matplotlib__matplotlib-26113",
"matplotlib__matplotlib-26122",
"matplotlib__matplotlib-26160",
"matplotlib__matplotlib-26184",
"matplotlib__matplotlib-26223",
"matplotlib__matplotlib-26249",
"matplotlib__matplotlib-26278",
"matplotlib__matplotlib-26285",
"matplotlib__matplotlib-26291",
"matplotlib__matplotlib-26300",
"matplotlib__matplotlib-26311",
"matplotlib__matplotlib-26341",
"matplotlib__matplotlib-26342",
"matplotlib__matplotlib-26399",
"matplotlib__matplotlib-26466",
"matplotlib__matplotlib-26469",
"matplotlib__matplotlib-26472",
"pallets__flask-4544",
"pallets__flask-4575",
"pallets__flask-4642",
"pytest-dev__pytest-8250",
]

def build(dataset_name, repo, limit=None):
    dataset = datasets.load_dataset(dataset_name)
    split = 'test'
    dataset = dataset[split]

    if repo:
        dataset = dataset.filter(lambda x: x['repo'] == repo)

    instance_ids = dataset['instance_id']
    
    instance_ids = [x for x in instance_ids if x in to_build]

    if limit:
        instance_ids = instance_ids[:limit]

    if instance_ids:
        print(f"Building images for {len(instance_ids)} instances for repo: {repo or 'all repos'}")

        prepare_images.main(
            dataset_name=dataset_name,
            split=split,
            instance_ids=instance_ids,
            max_workers=64,
            force_rebuild=False,
            open_file_limit=8192,
        )
    else:
        print(f"No instances to build for repo: {repo or 'all repos'}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build SWE-bench images')
    parser.add_argument('--repo', type=str, help='Repository to build images for (e.g., astropy/astropy)')
    parser.add_argument('--dataset', type=str, default='princeton-nlp/SWE-bench', help='Dataset name')
    parser.add_argument('--limit', type=int, help='Limit number of instances to build')
    
    args = parser.parse_args()
    
    build(args.dataset, args.repo, args.limit)
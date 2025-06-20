from swebench.harness import prepare_images
import datasets
import argparse

to_build = [
"matplotlib__matplotlib-23913",
"matplotlib__matplotlib-24189",
"matplotlib__matplotlib-24224",
"matplotlib__matplotlib-24971",
"matplotlib__matplotlib-25052",
"matplotlib__matplotlib-25281",
"matplotlib__matplotlib-25311",
"matplotlib__matplotlib-25332",
"matplotlib__matplotlib-25334",
"matplotlib__matplotlib-25346",
"matplotlib__matplotlib-25425",
"matplotlib__matplotlib-25551",
"matplotlib__matplotlib-26160",
"matplotlib__matplotlib-26278",
"matplotlib__matplotlib-26285",
"matplotlib__matplotlib-26341",
"matplotlib__matplotlib-26399",
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

    if limit and limit != -1:
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
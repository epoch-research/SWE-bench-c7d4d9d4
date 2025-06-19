from swebench.harness import prepare_images
import datasets
import argparse


def build(dataset_name, repo, limit=None):
    dataset = datasets.load_dataset(dataset_name)
    split = 'test'
    dataset = dataset[split]

    if repo:
        dataset = dataset.filter(lambda x: x['repo'] == repo)

    instance_ids = dataset['instance_id']

    if limit:
        instance_ids = instance_ids[:limit]

    print(f"Building images for {len(instance_ids)} instances for repo: {repo or 'all repos'}")

    prepare_images.main(
        dataset_name=dataset_name,
        split=split,
        instance_ids=instance_ids,
        max_workers=64,
        force_rebuild=False,
        open_file_limit=8192,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build SWE-bench images')
    parser.add_argument('--repo', type=str, help='Repository to build images for (e.g., astropy/astropy)')
    parser.add_argument('--dataset', type=str, default='princeton-nlp/SWE-bench', help='Dataset name')
    parser.add_argument('--limit', type=int, help='Limit number of instances to build')
    
    args = parser.parse_args()
    
    build(args.dataset, args.repo, args.limit)
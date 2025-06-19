from swebench.harness import prepare_images
import datasets


def build(dataset_name, repo, limit=None):
    dataset = datasets.load_dataset(dataset_name)
    split = 'test'
    dataset = dataset[split]

    if repo:
        dataset = dataset.filter(lambda x: x['repo'] == repo)

    instance_ids = dataset['instance_id']

    if limit:
        instance_ids = instance_ids[:limit]

    print(f"Building images for {len(instance_ids)} instances")

    prepare_images.main(
        dataset_name=dataset_name,
        split=split,
        instance_ids=instance_ids,
        max_workers=32,
        force_rebuild=False,
        open_file_limit=8192,
    )


if __name__ == '__main__':
    dataset_name = 'princeton-nlp/SWE-bench'
    repo: str | None = None
    build(dataset_name, repo)
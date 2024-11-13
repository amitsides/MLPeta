
ds = (ray.data.read_parquet("s3://my_bucket/input_data")
      .window(blocks_per_window=5)
      .map(cpu_intensive_preprocessing)
      .map_batches(gpu_intensive_inference, compute="actors", num_gpus=10)
      .repartition(10))
# Not needed:
ds.write_parquet("s3://my_bucket/output_predictions")
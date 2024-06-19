def batch_records(records, max_record_size=1024*1024, max_batch_size=5*1024*1024, max_records_per_batch=500):

    batches = []  
    current_batch = []
    current_batch_size = 0
    current_batch_count = 0
    
    for record in records:
        record_size = len(record.encode('utf-8'))
        
        if record_size > max_record_size:
            continue
        
        if (current_batch_size + record_size > max_batch_size or current_batch_count >= max_records_per_batch):
            batches.append(current_batch)
            current_batch = []
            current_batch_size = 0
            current_batch_count = 0
        
        current_batch.append(record)
        current_batch_size += record_size
        current_batch_count += 1

    if current_batch:
        batches.append(current_batch)
    
    return batches

example_records = ["a" * 500000, "b" * 1048577, "c" * 1000000, "d" * 2500000, "e" * 800000, "f" * 500000, "g" * 500000, "h" * 500000, "i" * 500000, "j" * 500000]

batched_records = batch_records(example_records)
for i, batch in enumerate(batched_records):
    print(f"Batch {i+1}: {[len(r) for r in batch]}")
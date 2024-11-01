import hashlib
import pathlib
import time

import rsa


def generate_keys():
    try:
        (pub_key, pri_key) = rsa.newkeys(512)
        string_pub_key = pub_key.save_pkcs1('PEM')
        string_pri_key = pri_key.save_pkcs1('PEM')
        with open("keys/Private_key.key", 'wb') as f1:
            f1.write(string_pri_key)
        with open("keys/Public_key.key", 'wb') as f2:
            f2.write(string_pub_key)
        return string_pri_key, string_pub_key
    except Exception as e:
        print(e)


def sign(object_to_be_used_for_signature):
    hashed_object = hash_object(object_to_be_used_for_signature)
    encoded_hashed_object = hashed_object.encode('UTF-8')
    serialized_key = retrieve_key_from_saved_file('Private')
    return rsa.sign(encoded_hashed_object, serialized_key, 'SHA-256')


def retrieve_key_from_saved_file(private_or_public):
    path = 'keys/' + private_or_public + "_key.key"
    file_path = pathlib.Path(path)
    with open(file_path, 'rb') as f:
        if private_or_public == 'Private':
            return rsa.PrivateKey.load_pkcs1(f.read())
        if private_or_public == "Public":
            return rsa.PublicKey.load_pkcs1(f.read())
        return None


def verify_signature(hashed_object, deserialized_signature, key):
    encoded_hashed_object = hashed_object.encode('UTF-8')
    serialized_signature = deserialized_signature
    return verify(encoded_hashed_object, serialized_signature, key)


def verify(hashed_credential, signature, pub_key):
    valid = False
    try:
        rsa.verify(hashed_credential, signature, pub_key)
        valid = True
    except Exception as e:
        print('a signature is found invalid!')
        print(e)
    return valid


def hash_object(entity):
    # hash something
    h = hashlib.sha256()
    h.update(str(entity).encode(encoding='UTF-8'))
    return h.hexdigest()


def hash_twice(entity):
    # hash something twice as for the merkle tree
    return hash_object(hash_object(entity))


def get_PoW_proof(block, targeted_hash, previous_hash):
    # print("Mining ... hold on")
    for nonce in range(1, 4000000000):
        block['Header']['Hash'] = hash_object([nonce, block['Header']['Timestamp'], block['Header']['previous_hash'], block['Header']['MR']])
        block['Header']['proof'] = nonce
        if pow_block_is_valid(block, targeted_hash, previous_hash):
            return block
    return None


def pow_block_is_valid(evaluated_block, targeted_hash, previous_hash):
    # check if the proposed hash fulfill the current puzzle difficulty
    condition1 = int(evaluated_block['Header']['Hash'], 16) <= int(targeted_hash, 16)
    # check if the previous hash in the proposed block is indeed the hash of the last accepted block
    condition2 = evaluated_block['Header']['previous_hash'] == previous_hash
    # check if the proposed block was generated during the past 2 hours (7200 seconds)
    condition3 = evaluated_block['Header']['Timestamp'] >= (time.time() - 7200)
    if condition1 and condition2 and condition3:
        return True
    return False
#
#
# def get_PoS_proof(block, staked_crypto):
#     block['Header']['proof'] = [staked_crypto, 'Miner_1']
#     return block


# def get_PoA_proof(block):
#
#     signature_bytes = sign(block['Body'])
#     if verify_signature(hash_object(block['Body']), signature_bytes, retrieve_key_from_saved_file('Public')):
#         print('Signature is valid')
#         block['Header']['proof'] = signature_bytes
#         print('Signature added to the block')
#
#     return block


def get_proof(block, consensus, parameter, previous_hash):
    if consensus == 1:
        return get_PoW_proof(block, parameter, previous_hash)
    # elif consensus == 2:
    #     return get_PoS_proof(block, parameter)
    # elif consensus == 3:
    #     return get_PoA_proof(block)

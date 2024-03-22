
import wave
import struct
from collections import defaultdict
from typing import Tuple, Dict

def read_xwav_header(xwav_file: str) -> Tuple[Dict, Dict, Dict]:
    """
    Read the header of an xwav file and return a Tuple of dictionaries containing the data
    :param xwav_file: string path to the xwav file
    :return: Three dictionaries, the first is the standard wav file header, the second is the harp chunk header, and the
    third is all the xwav chunk headers, usually about 30
    """

    chunk_data = {}
    harp_data = {}
    harp_subchunk_data = defaultdict(dict)
    with open(xwav_file, 'rb') as audio_file:
        chunk_data["chunk_id"] = struct.unpack('@4s', audio_file.read(4))[0]
        chunk_data["chunk_size"] = struct.unpack('@I', audio_file.read(4))[0]
        chunk_data["format"] = struct.unpack('@4s', audio_file.read(4))[0]
        chunk_data["subchunk1_id"] = struct.unpack('@4s', audio_file.read(4))[0]
        chunk_data["subchunk1_size"] = struct.unpack('@I', audio_file.read(4))[0]
        chunk_data["audio_format"] = struct.unpack('@H', audio_file.read(2))[0]
        chunk_data["num_channels"] = struct.unpack('@H', audio_file.read(2))[0]
        chunk_data["sample_rate"] = struct.unpack('@I', audio_file.read(4))[0]
        chunk_data["byte_rate"] = struct.unpack('@I', audio_file.read(4))[0]
        chunk_data["block_align"] = struct.unpack('@H', audio_file.read(2))[0]
        chunk_data["bits_per_sample"] = struct.unpack('@H', audio_file.read(2))[0]

        harp_data["harp_subchunk_id"] = struct.unpack('@4s', audio_file.read(4))[0]
        harp_data["harp_subchunk_size"] = struct.unpack('@I', audio_file.read(4))[0]
        harp_data["wav_version_number"] = struct.unpack('@B', audio_file.read(1))[0]
        harp_data["firmware_version_number"] = struct.unpack('@10s', audio_file.read(10))[0]
        harp_data["instrument_id"] = struct.unpack('@4s', audio_file.read(4))[0]
        harp_data["site_name"] = struct.unpack('@4s', audio_file.read(4))[0]
        harp_data["experiment_name"] = struct.unpack('@8s', audio_file.read(8))[0]
        harp_data["disk_sequence_number"] = struct.unpack('@B', audio_file.read(1))[0]
        harp_data["disk_serial_number"] = struct.unpack('@8s', audio_file.read(8))[0]
        harp_data["num_of_raw_files"] = struct.unpack('@H', audio_file.read(2))[0]
        harp_data["longitude"] = struct.unpack('@i', audio_file.read(4))[0] / 100_000  # file says it could be unsigned
        harp_data["latitude"] = struct.unpack('@i', audio_file.read(4))[0] / 100_000  # files says it could be unsigned
        harp_data["depth"] = struct.unpack('@H', audio_file.read(2))[0]
        harp_data["reserved"] = struct.unpack('@8s', audio_file.read(8))[0]

        for i in range(harp_data["num_of_raw_files"]):
            harp_subchunk_data[i]["year"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["month"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["day"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["hour"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["minute"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["second"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["ticks"] = struct.unpack('@H', audio_file.read(2))[0]
            harp_subchunk_data[i]["byte_loc"] = struct.unpack('@I', audio_file.read(4))[0]
            harp_subchunk_data[i]["byte_len"] = struct.unpack('@I', audio_file.read(4))[0]
            harp_subchunk_data[i]["write_length"] = struct.unpack('@I', audio_file.read(4))[0]
            harp_subchunk_data[i]["sample_rate"] = struct.unpack('@I', audio_file.read(4))[0]
            harp_subchunk_data[i]["gain"] = struct.unpack('@B', audio_file.read(1))[0]
            harp_subchunk_data[i]["padding"] = struct.unpack('@7p', audio_file.read(7))[0]

    return chunk_data, harp_data, harp_subchunk_data

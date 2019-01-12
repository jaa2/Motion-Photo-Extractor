""" Extracts a "motion photo" video from pictures created by Samsung Galaxy smartphones. """

import argparse
from os import path

def extract_motion_photo(filename, mp_fname=None):
    """ Extracts a motion photo from "filename" to "mp_fname" """
    with open(filename, "rb") as open_file:
        # Find a "motion photo marker" in the file
        contents = open_file.read()
        mp_marker = b"MotionPhoto_Data"
        pos = contents.find(mp_marker)

        if pos == -1:
            print("Error: Could not find motion photo data in this file.")
            return

        # Get file name of the motion photo if it is not yet defined
        if mp_fname is None:
            base_fname = path.splitext(filename)[0]
            mp_fname = base_fname + "_mp.mp4"

        # Open this file and write the output
        with open(mp_fname, "wb") as mp_file:
            mp_file.write(contents[pos + len(mp_marker):])
            print("Wrote motion photo to " + mp_fname + " successfully.")

def main():
    """ Main method; parses the arguments. """
    parser = argparse.ArgumentParser(description="Extract the \"motion photos\" from "
                                                 "pictures taken on a Samsung Galaxy "
                                                 "smartphone (S7 or newer).")
    parser.add_argument("image_file", type=str, help="Image file to open")
    parser.add_argument("output_file", type=str, nargs="?",
                        help="\"Motion photo\" video to output")

    args = parser.parse_args()
    extract_motion_photo(args.image_file, args.output_file)

if __name__ == "__main__":
    main()

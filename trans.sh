for filename in /storage/pooh/AISHELL3/test/wav/SSB0001/*; do
{
    ffmpeg -y -i $filename -acodec pcm_s16le -f s16le -ac 1 -ar 16000 $(basename $filename .wav).pcm;
}
done
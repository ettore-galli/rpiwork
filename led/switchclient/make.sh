OUTPUT_DIR=client-site

rm -rf $OUTPUT_DIR
npm run build
mv build $OUTPUT_DIR

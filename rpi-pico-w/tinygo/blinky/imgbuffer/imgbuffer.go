package imgbuffer

func ToImageBuffer(imageMap []byte, width int16) []byte {

	buffer := make([]byte, len(imageMap))
	wBytes := width / 8

	for index, imageByte := range imageMap {
		for i := int16(0); i < 8; i++ {
			bitshift := i
			mask := byte(1 << bitshift)
			imageBits := ((mask & imageByte) >> bitshift) << (7 - index%8)
			bytesBufferPos := int16(index)/8 + i*wBytes
			buffer[bytesBufferPos] |= imageBits
		}
	}

	return buffer

}

func ToSSD1306ImageBuffer(imageMap []byte) []byte {
	return ToImageBuffer(imageMap, 128)
}

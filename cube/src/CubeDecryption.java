import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class CubeDecryption {
    private static final String SECRET_KEY = ""; // it's a secret

    private final String cubeName;
    private final byte[] iv;
    private final byte[] cipherText;

    public CubeDecryption(String cubeName) {
        this.cubeName = cubeName;
        try (var cubeInputStream = getClass().getClassLoader().getResourceAsStream("cube/default_" + cubeName + ".CUBE.enc")) {
            if (cubeInputStream == null) {
                throw new IllegalArgumentException("Cube file not found: " + cubeName);
            }
            var cubeData = new String(cubeInputStream.readAllBytes(), StandardCharsets.UTF_8);
            var cubeDataParts = cubeData.split("]");
            if (cubeDataParts.length != 2) {
                throw new IllegalArgumentException("Invalid encrypted data format. Expected IV and ciphertext.");
            }
            iv = Base64.getDecoder().decode(cubeDataParts[0]);
            cipherText = Base64.getDecoder().decode(cubeDataParts[1]);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void decrypt() {
        try {
            // Prepare the secret key
            byte[] keyBytes = SECRET_KEY.getBytes(StandardCharsets.UTF_8);
            var keySpec = new SecretKeySpec(keyBytes, "AES");
            // Prepare the GCMParameterSpec
            var gcmParameterSpec = new GCMParameterSpec(128, iv); // 128-bit authentication tag
            // Initialize the Cipher for decryption
            var cipher = Cipher.getInstance("AES/GCM/NoPadding");
            cipher.init(Cipher.DECRYPT_MODE, keySpec, gcmParameterSpec);
            // Perform decryption
            byte[] plaintext = cipher.doFinal(cipherText);

            var outputStream = new FileOutputStream(cubeName + ".CUBE");
            outputStream.write(plaintext);
            outputStream.close();
        } catch (NoSuchPaddingException | IllegalBlockSizeException | NoSuchAlgorithmException |
                 InvalidAlgorithmParameterException | BadPaddingException | InvalidKeyException | IOException e) {
            throw new RuntimeException(e);
        }
    }
}

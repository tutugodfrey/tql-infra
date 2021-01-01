package test
import (
	"fmt"
	"testing"
	"time"

	http_helper "github.com/gruntwork-io/terratest/modules/http-helper"

	"github.com/gruntwork-io/terratest/modules/terraform"
)

func TestTerraformGcp(t *testing.T) {

	t.Parallel()
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		TerraformDir: "../infra",
         })

 defer terraform.Destroy(t, terraformOptions)

 terraform.InitAndApply(t, terraformOptions)
 externalIp := terraform.Output(t, terraformOptions, "external_ip")
 url := fmt.Sprintf("http://%s", externalIp)
 http_helper.HttpGetWithRetry(t, url, nil, 200, "Hello world!", 30, 5*time.Second)

}

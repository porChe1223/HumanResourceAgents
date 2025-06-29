import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as iam from 'aws-cdk-lib/aws-iam';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;
const TAVILY_API_KEY = process.env.TAVILY_API_KEY;

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // VPC（1つのAZのみ）
    const vpc = new ec2.Vpc(this, 'MyVpc', { maxAzs: 1 });

    // セキュリティグループ（SSH, HTTPを開放）
    const securityGroup = new ec2.SecurityGroup(this, 'MySecurityGroup', {
      vpc,
      allowAllOutbound: true,
      description: 'Allow SSH and HTTP',
    });

    securityGroup.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80), 'Allow HTTP');

    // EC2 IAMロール（SSM & EC2用）
    const role = new iam.Role(this, 'MyEc2Role', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'),
      ],
    });

    // ユーザーデータ
    const userData = ec2.UserData.forLinux();
    userData.addCommands(
      'sudo yum update -y',
      'sudo yum install -y git python3-pip',

      // uv をインストール
      'curl -LsSf https://astral.sh/uv/install.sh | sh',
      'export PATH="$HOME/.local/bin:$PATH"',

      // クローン
      'cd /home/ec2-user',
      'git clone https://github.com/porChe1223/HumanResourceAgents.git',

      // 依存解決
      'cd HumanResourceAgents/src',
      'uv venv .venv',
      'uv add -r requirements.txt',

      // 環境変数
      `export OPENAI_API_KEY=${OPENAI_API_KEY}`,
      `export GOOGLE_API_KEY=${GOOGLE_API_KEY}`,
      `export TAVILY_API_KEY=${TAVILY_API_KEY}`,

      // アプリ起動
      'uv run chainlit run main.py --host 0.0.0.0 --port 8080'
    );

    // EC2インスタンス
    new ec2.Instance(this, 'MyAppServer', {
      vpc,
      role,
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
      machineImage: ec2.MachineImage.latestAmazonLinux2023(),
      securityGroup,
      userData,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      associatePublicIpAddress: true,
    });
  }
}

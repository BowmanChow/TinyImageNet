class ConvNet(nn.Module):
    def __init__(self,):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            # 64
            nn.Conv2d(in_channels=3, out_channels=128,
                      kernel_size=3, padding=1),
            # 64
            nn.ReLU(),
            # nn.MaxPool2d(kernel_size=2, padding=0)
            #
        )
        self.layer2 = nn.Sequential(
            # 64
            nn.Conv2d(in_channels=128, out_channels=320,
                      kernel_size=3, padding=1, stride=2),
            # 32
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, padding=0)
            # 15
        )
        self.layer3 = nn.Sequential(
            # 15
            nn.Conv2d(in_channels=320, out_channels=320, kernel_size=2),
            # 14
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, padding=0)
            # 7
        )
        self.layer4 = nn.Sequential(
            # 7
            nn.Conv2d(in_channels=320, out_channels=128, kernel_size=2),
            # 6
        )
        self.layer5 = nn.Sequential(
            # 6
            nn.Linear(in_features=4608, out_features=2048),
            nn.ReLU(),
            nn.Linear(in_features=2048, out_features=1024),
            nn.ReLU(),
            nn.Linear(in_features=1024, out_features=100)
        )

    def forward(self, input):
        out = self.layer1(input)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = out.reshape(out.size(0), -1)
        out = self.layer5(out)
        return out


convNet = ConvNet()
print(convNet)
